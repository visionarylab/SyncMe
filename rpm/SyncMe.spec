Name:           SyncMe
Version:        0.3
Release:        1%{?dist}
Summary:        Application to unify the synchronization of Dropbox and Google Drive

License:        GPLv3
URL:            https://github.com/AdrianBZG/SyncMe/
Source0:        SyncMe-0.3.tar.gz

BuildRequires:  qt5-qtbase-devel qt5-qtwebkit-devel
Requires:       qt5-qtbase qt5-qtwebkit openssl

%description
SyncMe is a cross-platform application (Linux, Windows, Mac) written in Qt5
and C++ with the main goal of unify the synchronization of Dropbox and
Google Drive platforms into a single application, allowing you to manage
all your files easily.


%prep
%setup -q


%build
mkdir build
cd build
qmake-qt5 ../src/SyncMe/SyncMe.pro
make

%install
#rm -rf $RPM_BUILD_ROOT
#%make_install
install -m 755 -d %{buildroot}/%{_bindir}
install -m 755 build/SyncMe %{buildroot}/%{_bindir}/SyncMe



%files
%{_bindir}/*

%doc
%license LICENSE

%changelog
* Fri May  6 2016 Daniel García Moreno <danigm@wadobo.com> -- 0.3.1%{?dist}
- Initial version of the package
