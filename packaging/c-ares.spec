Name:       c-ares
Summary:    A library that performs asynchronous DNS operations
Version:    1.7.4
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://c-ares.haxx.se/
Source0:    http://c-ares.haxx.se/c-ares-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig


%description
c-ares is a C library that performs DNS requests and name resolves 
asynchronously. c-ares is a fork of the library named 'ares', written 
by Greg Hudson at MIT.



%package devel
Summary:    Development files for c-ares
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the header files and static libraries needed to
compile applications or shared objects that use c-ares.



%prep
%setup -q -n %{name}-%{version}

%build

%configure --disable-static \
    --enable-shared \
    --disable-dependency-tracking

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
%doc README README.cares
%{_libdir}/*.so.*


%files devel
%defattr(-,root,root,-)
%defattr(-, root, root, 0755)
%{_includedir}/ares.h
%{_includedir}/ares_build.h
%{_includedir}/ares_dns.h
%{_includedir}/ares_rules.h
%{_includedir}/ares_version.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libcares.pc
%doc %{_mandir}/man3/ares_*
