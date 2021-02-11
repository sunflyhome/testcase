# SPEC file overview:
# https://docs.fedoraproject.org/en-US/quick-docs/creating-rpm-packages/#con_rpm-spec-file-overview
# Fedora packaging guidelines:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/


Name:		printAweSome	
Version:	1
Release:	0
Summary:	printAweSome	

License:	GPL	
URL:		GPL		
Source0: 	printAweSome-1.0.tar.gz	


%description
TEST PrintAweSome
%prep
%setup -q
%build

%install
install -m 0755 -d $RPM_BUILD_ROOT/etc/printAweSome
install -m 0755 printAweSome.sh $RPM_BUILD_ROOT/etc/printAweSome/printAweSome.sh

%files
/etc/printAweSome
/etc/printAweSome/printAweSome.sh
%dir /etc/printAweSome
%defattr(-,root,root,-)
/etc/printAweSome/printAweSome.sh

%post
chmod 755 -R /etc/printAweSome