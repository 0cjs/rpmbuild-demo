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
# %setup -q wants to unpack a tar file, which is not what we want;
# let's just emulate what it does.
#
# rpmbuild will make BUILD our CWD at the start
rm -rf ct1
mkdir -p ct1
cp ../SOURCES/ct1 ./ct1/

%build
false

%install
false

%clean
rm -rf $RPM_BUILD_ROOT

%files
