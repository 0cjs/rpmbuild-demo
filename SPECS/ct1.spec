Name: ct1
Summary: Cynic-net Test Package 1

#Group: Test
%define version 0.0
Version: %{version}
Release: 1

License: hahaha
#URL: https://github.com/0cjs/rpmbuild-demo.git

#Provides: ct1
#Source: ct1
#Prefix: /tmp
#Buildroot: /tmp/ct1-build

%description
This is a test. This is only a test. Had this been a real package, uh....

%prep
false

%build
false

%install
false

%clean
rm -rf $RPM_BUILD_ROOT

%files
