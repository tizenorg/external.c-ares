Name:       c-ares
Summary:    library for asynchronous name resolves (development files)
Version: 1.7.4
Release:    2
Group:      System/Libraries
License:    MIT
Source0:    %{name}-%{version}.tar.gz
Source1001: c-ares.manifest
BuildRequires:  cmake
BuildRequires:  gettext-devel

%description
library for asynchronous name resolves (development files)


%package devel 
Summary:    library for asynchronous name resolves (development files) (Developement)
Group:      Development/Languages
Requires:   %{name} = %{version}-%{release}

%description devel
library for asynchronous name resolves (development files) (Developement)

%prep
%setup -q
cp %{SOURCE1001} .

%build
./buildconf
./configure --prefix=/usr --enable-shared --enable-symbol-hiding
make %{?_smp_flags}

%install
%make_install

%remove_docs

mkdir -p %{buildroot}/usr/share/license
cp %{_builddir}/%{buildsubdir}/LICENSE.MIT %{buildroot}/usr/share/license/%{name}

%files
%manifest %{name}.manifest
/usr/share/license/%{name}
/usr/lib/libcares.so.2
/usr/lib/libcares.so.2.0.0

%files devel 
/usr/include/*.h
/usr/lib/libcares.so
/usr/lib/pkgconfig/libcares.pc

