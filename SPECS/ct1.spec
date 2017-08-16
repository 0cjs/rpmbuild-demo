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
cd ct1
true            # Nothing to build

%install
# rpmbuild has created $RPM_BUILD_ROOT (`BUILDROOT/ct1-0.0-1.x86_64/`) for us.
# Our cwd is BUILD as usual
mkdir -p $RPM_BUILD_ROOT/tmp/ct
cp ct1/ct1 $RPM_BUILD_ROOT/tmp/ct/
# Uncomment the following to trigger detection of an unpackaged file.
#touch $RPM_BUILD_ROOT/tmp/ct/z

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/tmp/ct/ct1
