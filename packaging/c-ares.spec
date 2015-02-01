Name:       c-ares
Summary:    library for asynchronous name resolves (development files)
Version:    1.10.0_4
Release:    1
Group:      System/Libraries
License:    MIT
Source0:    %{name}-%{version}.tar.gz
Source1001: c-ares.manifest
Patch1:     prevent_fix.patch
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
%patch1 -p1

%build
./buildconf
./configure --prefix=/usr --enable-shared --enable-symbol-hiding
make %{?_smp_flags}

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}/usr/share/
mkdir -p %{buildroot}/usr/share/license
cp LICENSE %{buildroot}/usr/share/license/%{name}

%remove_docs

%files
%manifest %{name}.manifest
/usr/lib/libcares.so.2
/usr/lib/libcares.so.2.1.0
/usr/share/license/%{name}

%files devel 
/usr/include/*.h
/usr/lib/libcares.so
/usr/lib/pkgconfig/libcares.pc

