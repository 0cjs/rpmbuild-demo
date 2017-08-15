rpmbuild-demo
=============

This repo serves as both a record of my mucking about with `rpmbuild`
and some documentation on how to use it.


Directory Structure
-------------------

The "all my sources, specs and build stuff" directory defaults to
`/usr/src/redhat`, but can be changed by setting the `%_topdir` macro
(as we do in the `~/.rpmmacros` file set up by the
[`build-rpms`](./build-rpms) script, which points it to this
checkout). The only required stuff is some sort of source material in
`SOURCES` and some spec files in `SPECS`. The other directories
(`BUILD`, `RPMS` and `SRPMS`) will be created automatically. As will
`BUILDROOT`, not mentioned in the Fedora handbook.


References
----------

* [Fedora RPM Guide Edition 0][fedora-rpmguide-0]
* [Set Up an RPM Build Environment under CentOS][centos-howto-rpmbuild]

[fedora-rpmguide-0]: https://docs.fedoraproject.org/en-US/Fedora_Draft_Documentation/0.1/html/RPM_Guide/index.html
[centos-howto-rpmbuild]: https://wiki.centos.org/HowTos/SetupRpmBuildEnvironment
