#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : uhttpmock
Version  : 0.5.1
Release  : 4
URL      : https://github.com/pwithnall/uhttpmock/archive/0.5.1.tar.gz
Source0  : https://github.com/pwithnall/uhttpmock/archive/0.5.1.tar.gz
Summary  : HTTP web service mocking library
Group    : Development/Tools
License  : LGPL-2.1
Requires: uhttpmock-lib
Requires: uhttpmock-data
BuildRequires : autoconf-archive-dev
BuildRequires : docbook-xml
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(libsoup-2.4)

%description
uhttpmock
=========
uhttpmock is a project for mocking web service APIs which use HTTP or HTTPS. It
provides a library, libuhttpmock, which implements recording and playback of
HTTP requestâresponse traces.

%package data
Summary: data components for the uhttpmock package.
Group: Data

%description data
data components for the uhttpmock package.


%package dev
Summary: dev components for the uhttpmock package.
Group: Development
Requires: uhttpmock-lib
Requires: uhttpmock-data
Provides: uhttpmock-devel

%description dev
dev components for the uhttpmock package.


%package lib
Summary: lib components for the uhttpmock package.
Group: Libraries
Requires: uhttpmock-data

%description lib
lib components for the uhttpmock package.


%prep
%setup -q -n uhttpmock-0.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1494860682
%autogen --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1494860682
rm -rf %{buildroot}
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
/usr/lib64/libuhttpmock-0.0.so.0.2.1
