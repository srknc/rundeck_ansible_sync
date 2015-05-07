# rundeck_ansible_sync

script syncs ansible inventory hosts with rundeck nodes.

steps;
- list ansible hosts greping the inventory file or files inside folder
- parse hostname and ip address 
- prepare xml file for rundeck resources.xml file
- check xml integrity 
- update rundeck resource.xml file


below configuration parameters should be checked before execution;
- project_name    = 'product'
- resource_file   = '/opt/rundeck/projects/'+project_name+'/etc/resources.xml'
- host_file       = '/opt/ansible/hosts/*'
- #host_file      = '/opt/ansible/hosts'
- rundeck_node_user = 'root'
