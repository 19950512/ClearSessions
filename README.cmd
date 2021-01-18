# SCRIPT QUE TENTA REMOVER OS ARQUIVOS DE SESSÃO VAZIOS.

Isso para limpar e recuperar espaço em disco. Isso deve ser executado periodicamente.

# ENV
PASSWORD=senha_sudo

# CRON

em /etc/cron.d/<meu_cron>

# run script every 24 hours
0 */24 * * *  <nome_usuario>  python3 /diretorio/script.py

# run script after system (re)boot
@reboot       <nome_usuario> python3 /diretorio/script.py
