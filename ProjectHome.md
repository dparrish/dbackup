dbackup is a disk-based client-server backup system for Linux or other UNIX systems.

It works on the principal that disks are cheaper and more reliable than tapes.

Backups are started by cron probably on a daily basis by the client. The client backs up individual filesystems / directories with tar and sends the result to the server, which stores them in a simple tree-based directory structure.

Restores are trivial, either by using the supplied restore client, or by simply copying the appropriate tar files off the server and uncompressing them.

  * Backup very large filesystems as long as you have the disk space
  * Works with very large numbers of servers / filesystems
  * No state is kept on the client, it’s all on the server
  * Backup to multiple backup servers in round-robin
  * Configuration can be global or per-server
  * Authentication for client restores (optional)
  * Supports optional gzip or bzip2 compression
  * Supports client-side gpg encryption
  * Trivial procedure for restores
  * Daily / Full incremental backups
