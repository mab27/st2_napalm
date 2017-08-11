from jinja2 import Template
from st2actions.runners.pythonrunner import Action


class renderCfg(Action):
    def run(self, j2_loaction, feature_set, driver, router_Id, local_ASN, remote_ASN, peer_IP, remote_hostname):

        path_to_template_file = j2_loaction + "/" + feature_set + "/" + driver + ".j2"
        path_to_rendered_file = "/home/mab/automation/generated_files/" + driver +"_" + feature_set + "_.txt"


        template_file=open(path_to_template_file)
        s=template_file.read()
        template=Template(s)
        rendering = template.render(router_Id=router_Id, local_ASN=local_ASN, remote_ASN=remote_ASN, peer_IP=peer_IP, remote_hostname=remote_hostname)

        file=open(path_to_rendered_file,"w")
        file.write(rendering)
        file.close()

        result = dict.fromkeys(['rendered_file'])
        result['rendered_file']=path_to_rendered_file

        return result