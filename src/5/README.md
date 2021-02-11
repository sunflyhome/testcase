#Build Log

rpmbuild -ba SPECS/printAweSome.spec
Executing(%prep): /bin/sh -e /var/tmp/rpm-tmp.4nhvHR
+ umask 022
+ cd /home/ec2-user/rpmbuild/BUILD
+ cd /home/ec2-user/rpmbuild/BUILD
+ rm -rf printAweSome-1
+ /usr/bin/tar -xf -
+ /usr/bin/gzip -dc /home/ec2-user/rpmbuild/SOURCES/printAweSome-1.0.tar.gz
+ STATUS=0
+ '[' 0 -ne 0 ']'
+ cd printAweSome-1
+ /usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
+ exit 0
Executing(%build): /bin/sh -e /var/tmp/rpm-tmp.ylv6p1
+ umask 022
+ cd /home/ec2-user/rpmbuild/BUILD
+ cd printAweSome-1
+ exit 0
Executing(%install): /bin/sh -e /var/tmp/rpm-tmp.GwMI9a
+ umask 022
+ cd /home/ec2-user/rpmbuild/BUILD
+ '[' /home/ec2-user/rpmbuild/BUILDROOT/printAweSome-1-0.x86_64 '!=' / ']'
+ rm -rf /home/ec2-user/rpmbuild/BUILDROOT/printAweSome-1-0.x86_64
++ dirname /home/ec2-user/rpmbuild/BUILDROOT/printAweSome-1-0.x86_64
+ mkdir -p /home/ec2-user/rpmbuild/BUILDROOT
+ mkdir /home/ec2-user/rpmbuild/BUILDROOT/printAweSome-1-0.x86_64
+ cd printAweSome-1
+ install -m 0755 -d /home/ec2-user/rpmbuild/BUILDROOT/printAweSome-1-0.x86_64/etc/printAweSome
+ install -m 0755 printAweSome.sh /home/ec2-user/rpmbuild/BUILDROOT/printAweSome-1-0.x86_64/etc/printAweSome/printAweSome.sh
+ /usr/lib/rpm/find-debuginfo.sh --strict-build-id -m --run-dwz --dwz-low-mem-die-limit 10000000 --dwz-max-die-limit 110000000 /home/ec2-user/rpmbuild/BUILD/printAweSome-1
/usr/lib/rpm/sepdebugcrcfix: Updated 0 CRC32s, 0 CRC32s did match.
+ '[' '%{buildarch}' = noarch ']'
+ QA_CHECK_RPATHS=1
+ case "${QA_CHECK_RPATHS:-}" in
+ /usr/lib/rpm/check-rpaths
+ /usr/lib/rpm/check-buildroot
+ /usr/lib/rpm/redhat/brp-compress
+ /usr/lib/rpm/redhat/brp-strip-static-archive /usr/bin/strip
+ /usr/lib/rpm/brp-python-bytecompile /usr/bin/python 1
+ /usr/lib/rpm/redhat/brp-python-hardlink
+ /usr/lib/rpm/redhat/brp-java-repack-jars
Processing files: printAweSome-1-0.x86_64
warning: File listed twice: /etc/printAweSome
warning: File listed twice: /etc/printAweSome/printAweSome.sh
warning: File listed twice: /etc/printAweSome/printAweSome.sh
Provides: printAweSome = 1-0 printAweSome(x86-64) = 1-0
Requires(interp): /bin/sh
Requires(rpmlib): rpmlib(CompressedFileNames) <= 3.0.4-1 rpmlib(FileDigests) <= 4.6.0-1 rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires(post): /bin/sh
Requires: /bin/env
Processing files: printAweSome-debuginfo-1-0.x86_64
Provides: printAweSome-debuginfo = 1-0 printAweSome-debuginfo(x86-64) = 1-0
Requires(rpmlib): rpmlib(FileDigests) <= 4.6.0-1 rpmlib(PayloadFilesHavePrefix) <= 4.0-1 rpmlib(CompressedFileNames) <= 3.0.4-1
Checking for unpackaged file(s): /usr/lib/rpm/check-files /home/ec2-user/rpmbuild/BUILDROOT/printAweSome-1-0.x86_64
Wrote: /home/ec2-user/rpmbuild/SRPMS/printAweSome-1-0.src.rpm
Wrote: /home/ec2-user/rpmbuild/RPMS/x86_64/printAweSome-1-0.x86_64.rpm
Wrote: /home/ec2-user/rpmbuild/RPMS/x86_64/printAweSome-debuginfo-1-0.x86_64.rpm
Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.ALgFdP
+ umask 022
+ cd /home/ec2-user/rpmbuild/BUILD
+ cd printAweSome-1
+ /usr/bin/rm -rf /home/ec2-user/rpmbuild/BUILDROOT/printAweSome-1-0.x86_64
+ exit 0
