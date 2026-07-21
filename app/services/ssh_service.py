import paramiko


def execute_command(host, username, key_path, command):

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(
        hostname=host,
        username=username,
        key_filename=key_path
    )

    stdin, stdout, stderr = ssh.exec_command(command)

    output = stdout.read().decode()
    error = stderr.read().decode()

    ssh.close()

    return {
        "output": output,
        "error": error
    }