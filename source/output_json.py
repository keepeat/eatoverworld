# -*-encoding:utf-8 -*-

# 把 poi 转换为 json 方便搜索引擎

import os
import sys
import re
import json



SOURCE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(SOURCE_DIR,'exts'))
from gaode import Gaode



def visit_poi_file(fpath):

	poi_string_list = []
	pointer = -1
	with open(fpath,'r') as f :
		for line in f:
			if line.startswith(".. poi::"):

				state = 'POI'
				pointer +=1
				poi_string_list.append(".. poi::")
			else:

				if re.search("^\s+",line):
					# 以 空开头，说明在 poi directive 下。
					if poi_string_list and pointer>-1 and state=='POI':
						poi_string_list[pointer]+=line

				elif re.search("^\S+",line):
					# 以字符串开头，说明poi 结束。
		
					state = None 

	pois = []
	for poi_s in poi_string_list:
		name = re.search(":name:(.*)",poi_s).groups()[0].strip()
		address = re.search(":address:(.*)",poi_s).groups()[0].strip()
		link = re.search(":link:(.*)",poi_s).groups()[0].strip()
		scene = re.search(":scene:(.*)",poi_s).groups()[0].strip()
		recommand = re.search(":recommend:\s(\S+)",poi_s).groups()[0].strip()
		geo_address = Gaode.address2dest(address)
		pois.append(dict(
			name=name,
			address=address,
			link=link,
			scene=scene.split(','),
			recommand = recommand.split(','),
			geo_address = geo_address.split(',')
			)
			)
	return pois



def main():

	pois = []
	for p_tuple in os.walk(SOURCE_DIR):
		if p_tuple[1]:
			continue
		for f in p_tuple[2]:
			if re.search("\.rst$",f):		
				path = os.path.join(p_tuple[0],f)
				pois.extend(visit_poi_file(path))

	print(json.dumps({"pois":pois}))






if __name__=="__main__":

	main()




