#!/usr/bin/env python
import sys
import resource
import time
import subprocess
import os

AIDA_DIR = os.path.expanduser('~/aida')
JAR_PATH = 'target/aida-3.0.5-SNAPSHOT-jar-with-dependencies.jar'

def get_aida_locations():

	# Read the aida path from the aidarc config file
	rc_data = None
	try:
		rc_path = os.path.expanduser('~/.aidarc')
		rc_data = json.loads(open(rc_path).read())
		print 'loaded rc file from %s' % rc_path

	# Fail if the aidarc file has invalid json
	except ValueError:
		print 'aidarc file has invalid json'
		sys.exit(1)

	# Tolerate missing rc_file silently
	except IOError:
		print 'no rc file found, using defaults.'
		pass

	# If we loaded an rc_file, try to obtain path information from it
	aida_dir = AIDA_DIR
	jar_path = JAR_PATH
	main_class = MAIN_CLASS
	if rc_data is not None:
		if 'aida_dir' in rc_data:
			aida_dir = rc_data['aida_dir']

		if 'jar_path' in rc_data:
			jar_path = rc_data['jar_path']

		if 'main_class' in rc_data:
			main_claSS = rc_data['main_class']

	print 'aida_dir: %s' % aida_dir
	print 'jar_path: %s' % jar_path
	print 'main_class: %s' % main_class

	return aida_dir, jar_path, main_class


def run(
	dir=None,
	file=None,
	threads=1,
	method='LOCAL',
	output_format='JSON'
):

	# Get the aida directory and relative location of the jar file
	aida_dir, jar_path, main_class = get_aida_locations()

	# Aida has to be run from it's source directory
	cwd = os.getcwd()
	os.chdir(aida_dir)

	# Compose the shell command
	cmd = [
		'java', 
		'-Xmx64G', 
		'-cp', jar_path,
		main_class,
		'-c', '%d' % threads
		'-t', method, 
		'-o', output_format
	]

	# Workout the input file / directory
	if dir is not None and file is not None:
		raise ValueError('Specify either `dir` or `file`, but not both.')
	if dir is not None:
		cmd.extend(['-d -i', dir])
	elif file is not None:
		cmd.extend(['-i', file])
	else:
		raise ValueError('An input `dir` or `file` must be specified.')

	# Run Aida
	start_time = time.time()
	ps = subprocess.Popen(' '.join(cmd), shell=True)
	ps.wait()
	end_time = time.time()

	# Go back to original working directory
	os.chdir(cwd)

	mem_usage_kilobytes = resource.getrusage(resource.RUSAGE_CHILDREN)[2]
	mem_usage_gigabytes = mem_usage_kilobytes / 1000000.
	print 'Max ram resident usage: %2.3fg' % (mem_usage_gigabytes)
	print 'Total time needed: %ds' % (end_time - start_time)


if __name__=="__main__":
	test_method()

