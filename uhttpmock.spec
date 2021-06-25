#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : uhttpmock
Version  : 0.5.3
Release  : 12
URL      : https://gitlab.com/uhttpmock/uhttpmock/-/archive/0.5.3/uhttpmock-0.5.3.tar.gz
Source0  : https://gitlab.com/uhttpmock/uhttpmock/-/archive/0.5.3/uhttpmock-0.5.3.tar.gz
Summary  : HTTP web service mocking library
Group    : Development/Tools
License  : LGPL-2.1
Requires: uhttpmock-data = %{version}-%{release}
Requires: uhttpmock-lib = %{version}-%{release}
Requires: uhttpmock-license = %{version}-%{release}
BuildRequires : autoconf-archive-dev
BuildRequires : docbook-xml
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : vala

%description
uhttpmock
=========
uhttpmock is a project for mocking web service APIs which use HTTP or HTTPS. It
provides a library, libuhttpmock, which implements recording and playback of
HTTP request–response traces.

%package data
Summary: data components for the uhttpmock package.
Group: Data

%description data
data components for the uhttpmock package.


%package dev
Summary: dev components for the uhttpmock package.
Group: Development
Requires: uhttpmock-lib = %{version}-%{release}
Requires: uhttpmock-data = %{version}-%{release}
Provides: uhttpmock-devel = %{version}-%{release}
Requires: uhttpmock = %{version}-%{release}

%description dev
dev components for the uhttpmock package.


%package lib
Summary: lib components for the uhttpmock package.
Group: Libraries
Requires: uhttpmock-data = %{version}-%{release}
Requires: uhttpmock-license = %{version}-%{release}

%description lib
lib components for the uhttpmock package.


%package license
Summary: license components for the uhttpmock package.
Group: Default

%description license
license components for the uhttpmock package.


%prep
%setup -q -n uhttpmock-0.5.3
cd %{_builddir}/uhttpmock-0.5.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624659282
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1624659282
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/uhttpmock
cp %{_builddir}/uhttpmock-0.5.3/COPYING %{buildroot}/usr/share/package-licenses/uhttpmock/caeb68c46fa36651acf592771d09de7937926bb3
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Uhm-0.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/libuhttpmock-0.0/uhttpmock/uhm-resolver.h
/usr/include/libuhttpmock-0.0/uhttpmock/uhm-server.h
/usr/include/libuhttpmock-0.0/uhttpmock/uhm-version.h
/usr/include/libuhttpmock-0.0/uhttpmock/uhm.h
/usr/lib64/libuhttpmock-0.0.so
/usr/lib64/pkgconfig/libuhttpmock-0.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libuhttpmock-0.0.so.0
/usr/lib64/libuhttpmock-0.0.so.0.2.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/uhttpmock/caeb68c46fa36651acf592771d09de7937926bb3
