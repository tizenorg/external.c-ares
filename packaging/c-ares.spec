#sbs-git:slp/pkgs/c/c-ares c-ares 1.7.4 a598a0be73d9a97a303887c6e186d067256686eb
Name:       c-ares
Summary:    library for asynchronous name resolves (development files)
Version: 1.7.4
Release:    1
Group:      TO_BE_FILLED
License:    TO_BE_FILLED
Source0:    %{name}-%{version}.tar.gz
Source1001: packaging/c-ares.manifest 
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(dlog)
BuildRequires:  pkgconfig(vconf)

BuildRequires:  cmake
BuildRequires:  gettext-devel

%description
library for asynchronous name resolves (development files)


%package devel 
Summary:    library for asynchronous name resolves (development files) (Developement)
Group:      TO_BE_FILLED 
Requires:   %{name} = %{version}-%{release}

%description devel
library for asynchronous name resolves (development files) (Developement)

%prep
%setup -q

%build
cp %{SOURCE1001} .
./buildconf
./configure --prefix=/usr --enable-shared --enable-symbol-hiding
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
%remove_docs
%post

%postun


%files
%manifest c-ares.manifest
%defattr(-,root,root,-)
/usr/lib/libcares.so.2
/usr/lib/libcares.so.2.0.0

%files devel 
%manifest c-ares.manifest
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib/libcares.so
/usr/lib/pkgconfig/libcares.pc

