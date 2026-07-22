import os
import paramiko

def execute_command(host, username, key_path, command):

    print("HOST:", host)
    print("USERNAME:", username)
    print("KEY:", key_path)
    print("EXISTS:", os.path.exists(key_path))

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(
        hostname=host,
        username=username,
        key_filename=key_path,
        look_for_keys=False,
        allow_agent=False,
        timeout=15
    )

    stdin, stdout, stderr = ssh.exec_command(command)

    output = stdout.read().decode()
    error = stderr.read().decode()

    ssh.close()

    return {
        "output": output,
        "error": error
    }
def deploy_container(image, container_name):

    return f"""
docker pull {image} &&
docker stop {container_name} || true &&
docker rm {container_name} || true &&
docker run -d --name {container_name} -p 80:80 {image}
"""