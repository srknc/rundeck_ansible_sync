#!/usr/bin/python
import sys
import subprocess
from lxml import etree

working_folder	='/tmp/rundeck_ansible_sync/'
project_name 	= 'product'
resource_file 	= '/opt/rundeck/projects/'+project_name+'/etc/resources.xml'
host_file 	= '/opt/ansible/hosts/*'
#host_file 	= '/opt/ansible/hosts'
rundeck_node_user = 'root'

def list_hosts():
	command = "cat "+host_file+" | grep 'ansible_ssh_host' | grep -v '$^'  | grep -v '#'"
	output = subprocess.check_output(command, shell=True)
	output=output.replace(" ", "")
	output=output.replace("\t", "")
	output_lines=output.split('\n')
	#print output_lines
	data=[]
	for host in output_lines:
		host_data=host.split('ansible_ssh_host')
		if len(host_data) != 2:
			continue
		hostname = host_data[0]
		ansible_ssh_host=host_data[1]
		ansible_ssh_host = ansible_ssh_host.replace('=','')
		host_data[1]=host_data[1].replace('=','')
		data.append(host_data)

	return data



def prepare_resource_content(data):
	content = "<?xml version='1.0' encoding='UTF-8'?>\n<project>\n"
	for i in data:
		content = content + "<node name='"+i[0]+"' description='"+i[0]+"'  hostname='"+i[1]+"' username='"+rundeck_node_user+"'/>\n"
	content = content + '</project>'
	try:
		parser = etree.XMLParser(dtd_validation=True)
		return content
	except:
		sys.exit()


def update_file(content):
	file = open(resource_file,'w')
	file.write(content)
	file.close
     


if __name__ == "__main__":
	print 'getting host informations...'
	data = list_hosts()

	print 'preparing resource file content'
	content = prepare_resource_content(data)

	print 'updating resorces file ('+resource_file+')'
	update_file(content)

	print 'finished'



