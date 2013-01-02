#! /bin/bash
 
mysql -u root -e 'DROP SCHEMA `linux-admin-toolkit`'
mysql -u root -e 'CREATE SCHEMA `linux-admin-toolkit`'

#cd /home/sysadmin/workspace/linux-admin-toolkit/frontend/

echo "set proper directory"
exit

python manage.py syncdb --noinput

python manage.py createsuperuser --username sysadmin --email sysadmin@linux-admin-toolkit.com --noinput

#delme hashes to -> pbkdf2_sha256$10000$Q6pHBZBRK3X2$AHfB8wkd/qKpTFagSZ00UaHSkXpSq73RHGxHUrqm77M=
#includes escaped characters in hash
echo 'UPDATE `linux-admin-toolkit`.`auth_user` SET `password`='"'"pbkdf2_sha256\$10000\$Q6pHBZBRK3X2\$AHfB8wkd\/qKpTFagSZ00UaHSkXpSq73RHGxHUrqm77M="'"' WHERE `id`='"'"1"';" |mysql -u root


#echo <<Here_Doc_01
#from django.contrib.auth.models import User
#user = User.objects.create_user('view', 'viewonly@nodomain.com', 'view')
#user.save()
#Here_Doc_01

#create view only user

cat <<EOF | python manage.py shell
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
user = User.objects.create_user('view', 'viewonly@nodomain.com', 'view')
permission = Permission.objects.get(codename="change_physical")
user.user_permissions.add(permission)
permission = Permission.objects.get(codename="change_virtual")
user.user_permissions.add(permission)
user.save()
EOF

#python manage.py changepassword sysadmin
echo "Intialization completed. Now import data." 