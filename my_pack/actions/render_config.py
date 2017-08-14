from jinja2 import Template
from st2actions.runners.pythonrunner import Action


class render_config(Action):
    def run(self, j2_location, variables, function, device_id):

        # Prepare file locations for template and rendering
        driver = variables["driver"]
        path_to_template_file = j2_location + "/" + function + "/" + driver + ".j2"
        path_to_rendered_file = "~/automation/rendered_files/" + function + "_" + device_id + "_" + driver + "_.txt"

        # Prepare tempating
        template_file=open(path_to_template_file)
        s=template_file.read()
        template=Template(s)

        # Execute templating based on function value and variables verification
        if function = "cfg_ebgp":
            try:
                router_Id = variables["router_Id "]
            except:
                return (False, "Missing hostname in the variables object ")
            try:
                local_ASN = variables["local_ASN"]
            except:
                return (False, "Missing local ASN in the variables object ")
            try:
                remote_ASN = variables["remote_ASN"]
            except:
                return (False, "Missing remote ASN in the variables object ")
            try:
                peer_IP = variables["peer_IP"]
            except:
                return (False, "Missing peer IP in the variables object ")
            try:
                remote_hostname = variables["remote_hostname"]
            except:
                return (False, "Missing peer IP in the variables object ")
            rendering = template.render(router_Id=router_Id, local_ASN=local_ASN, remote_ASN=remote_ASN, peer_IP=peer_IP, remote_hostname=remote_hostname)

        # Write the result of rendering in the destination file
        file=open(path_to_rendered_file,"w")
        file.write(rendering)
        file.close()

        file=open(path_to_rendered_file,"r")
        file.close()

        # Provide the rendered file as an object
        result = dict.fromkeys(['rendered_file'])
        result['rendered_file']=path_to_rendered_file

        return result