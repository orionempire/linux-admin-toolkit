#! /bin/bash

#Version 00.00.10

##Install pip
#curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
#python get-pip.py

##AS ROOT -> Install Django and modules
#pip install Django
#pip install xlwt
#pip install xlrd

##archive old installs 
mkdir -p /etc/configuration_file_archive/linux-admin-toolkit
tar cvzf /etc/configuration_file_archive/linux-admin-toolkit/linux-admin-toolkit_`date +"%H-%M_%m-%d-%Y"`.tgz /opt/linux-admin-toolkit/ > /dev/null
rm -fr /opt/linux-admin-toolkit/
mv /var/linux-admin-toolkit/server_inventory_import_export.xls /var/linux-admin-toolkit/archive/server_inventory_import_export_`date +"%H-%M_%m-%d-%Y"`.xls 

 
service httpd stop
##Get and install the code
mkdir -p /opt/linux-admin-toolkit/
wget http://linux-admin-toolkit.googlecode.com/git/packages/linux-admin-toolkit_current.tgz
tar xvfz linux-admin-toolkit_current.tgz
mv linux-admin-toolkit /opt/
chown -R apache.apache /opt/linux-admin-toolkit/
rm -f linux-admin-toolkit_current.tgz


##Create the data location
mkdir  /var/linux-admin-toolkit/
chmod a+w /var/linux-admin-toolkit/
touch /etc/clusters
chmod a+w /etc/clusters 


grep -q -e 'linux-admin-toolkit' /etc/httpd/conf/httpd.conf || cat << 'EOF' >> /etc/httpd/conf/httpd.conf
<VirtualHost *:80>

    ServerName wsgi.djangoserver
    DocumentRoot /opt/linux-admin-toolkit/frontend

    <Directory /opt/linux-admin-toolkit/frontend>
        Order allow,deny
        Allow from all
    </Directory>

    WSGIScriptAlias / /opt/linux-admin-toolkit/frontend/frontend/wsgi.py

    Alias /static/admin/ /usr/lib/python2.6/site-packages/django/contrib/admin/static/admin/

    <Directory /usr/lib/python2.6/site-packages/django/contrib/admin/static/admin>
        Order deny,allow
        Allow from all
    </Directory>

</VirtualHost>
EOF

chkconfig httpd on
service httpd start

yum -y install xterm

rpm -Uvh http://linux-admin-toolkit.googlecode.com/git/packages/perl-X11-Protocol-0.56-4.el6.noarch.rpm
rpm -Uvh http://linux-admin-toolkit.googlecode.com/git/packages/perl-Tk-804.028-12.el6.x86_64.rpm
rpm -Uvh http://linux-admin-toolkit.googlecode.com/git/packages/clusterssh-3.28-2.el6.noarch.rpm

cd /opt/linux-admin-toolkit/frontend
python manage.py changepassword sysadmin

echo "To import data run...."
echo "cd /home/sysadmin/workspace" 
echo "tar --exclude='linux-admin-toolkit/.git' -cvzf  linux-admin-toolkit_current.tgz linux-admin-toolkit/ ; mv linux-admin-toolkit_current.tgz linux-admin-toolkit/packages/" 

