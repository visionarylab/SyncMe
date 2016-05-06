# RPM package spec file

## How to build the rpm package in fedora

 * Setting up the environment

```
# dnf install @development-tools
# dnf install fedora-packager
# dnf install rpmdevtools
```

 * Adding my user to mock group. MYUSER is a non-root user.

```
# usermod -a -G mock MYUSER
```

 * As MYUSER, setup the rpm dev tree

```
$ rpmdev-setuptree
```

 * Copy the .spec file to your SPECS folder and the code to the SOURCES
   folder

```
$ cp SyncMe/rpm/SyncMe.spec ~/rpmbuild/SPECS/
$ mv SyncMe SyncMe-VERSION
$ tar -czvf SyncMe-VERSION.tar.gz SyncMe-VERSION
$ cp SyncMe-VERSION.tar.gz ~/rpmbuild/SOURCES/
```

 * Update the .spec file incrementing the version and adding a new line in
   the changelog
 * Build the package

```
$ cd  ~/rpmbuild/SPECS/
$ rmpbuild -ba SyncMe.spec
```

 * If nothing fails the RPM should be in ~/rpmbuild/RPMS/
