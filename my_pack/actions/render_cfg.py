from jinja2 import Template
from st2actions.runners.pythonrunner import Action


class render_cfg(Action):
    def run(self, driver, router_Id, local_ASN, remote_ASN, peer_IP, remote_hostname):

        path_to_template_file = "/opt/stackstorm/packs/default/actions/template_files/template_ebgp_" + driver + ".j2"
        path_to_rendered_file = "/opt/stackstorm/packs/default/actions/rendered_files/cfg_ebgp_" + driver +"_" + router_Id + "_.txt"

        template_file=open(path_to_template_file)
        s=template_file.read()
        template=Template(s)
        rendering = template.render(router_Id=router_Id, local_ASN=local_ASN, remote_ASN=remote_ASN, peer_IP=peer_IP, remote_hostname=remote_hostname)

        file=open(path_to_rendered_file,"w")
        file.write(rendering)
        file.close()

        file=open(path_to_rendered_file,"r")
        file.close()

        result = dict.fromkeys(['rendered_file'])
        result['rendered_file']=path_to_rendered_file

        return result