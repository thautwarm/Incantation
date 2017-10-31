# compile .py to .pyc recursively.
import sys
import os
from flowpython.fp import flatten, flow_map, flow_filter, foreach
proj, newprojdir = sys.argv[1:]

def listdir(dir):
	if not os.path.isdir(dir):
		return dir
	files = os.listdir(dir)
	files = list(flow_map(.x->f"{dir}/{x}")(files))
	return flow_map(listdir)(files) ->> list

def get_pyfiles(dirs):
	return flatten(dirs) ->> flow_filter(.x->x.endswith('.py')) => list


py_compile = as-with newprojdir def as file def None where: 
	dir, name = os.path.split(file[:-3])
	pyc_file = f"{dir}/__pycache__/{name}.cpython-36.pyc"
	result_path = f"{newprojdir}/{dir}/{name}.pyc"
	try:
		os.makedirs(os.path.split(result_path)[0])
	except FileExistsError:
		pass
	os.system(f'python -m py_compile {file}')
	try:
		os.rename(pyc_file, result_path)
	except FileExistsError:
		with open(pyc_file, 'rb') as src, open(result_path, 'wb') as dist:
			dist.write(src.read())


def main(proj, newprojdir):
	proj ->> listdir => get_pyfiles => foreach(py_compile(newprojdir)) 

main(proj, newprojdir)
