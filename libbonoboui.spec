## don't replace ltmain.sh
%define __libtoolize echo

%define libxml2_version 2.4.12
%define orbit2_version 2.3.103
%define bonobo_activation_version 0.9.3.91
%define libbonobo_version 1.110.0
%define libgnomecanvas_version 1.110.0
%define libgnome_version 1.110.0
%define libart_lgpl_version 2.3.8
%define gtk2_version 1.3.13
%define libglade2_version 1.99.5.90

Summary: Bonobo user interface components
Name: libbonoboui
Version: 1.110.0
Release: 4
URL: http://ftp.gnome.org
Source0: %{name}-%{version}.tar.gz
Source2: bonoboui-fixed-ltmain.sh
License: LGPL
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-root

Requires: libxml2 >= %{libxml2_version}
Requires: ORBit2 >= %{orbit2_version}
Requires: bonobo-activation >= %{bonobo_activation_version}
Requires: libbonobo >= %{libbonobo_version}
Requires: libgnomecanvas >= %{libgnomecanvas_version}
Requires: libgnome >= %{libgnome_version}
Requires: libart_lgpl >= %{libart_lgpl_version}
Requires: gtk2 >= %{gtk2_version}
Requires: libglade2 >= %{libglade2_version}

BuildPreReq: libxml2-devel >= %{libxml2_version}
BuildPreReq: ORBit2-devel >= %{orbit2_version}
BuildPreReq: bonobo-activation-devel >= %{bonobo_activation_version}
BuildPreReq: libbonobo-devel >= %{libbonobo_version}
BuildPreReq: libgnomecanvas-devel >= %{libgnomecanvas_version}
BuildPreReq: libgnome-devel >= %{libgnome_version}
BuildPreReq: libart_lgpl-devel >= %{libart_lgpl_version}
BuildPreReq: gtk2-devel >= %{gtk2_version}
BuildPreReq: libglade2-devel >= %{libglade2_version}
BuildPreReq: intltool >= 0.14-1

%description

Bonobo is a component system based on CORBA, used by the GNOME
desktop.  libbonoboui contains the user interface related components
that come with Bonobo.

%package devel
Summary: Libraries and headers for libbonoboui
Group: Development/Libraries
Requires:	%name = %{version}
Requires: libxml2-devel >= %{libxml2_version}
Requires: ORBit2-devel >= %{orbit2_version}
Requires: bonobo-activation-devel >= %{bonobo_activation_version}
Requires: libbonobo-devel >= %{libbonobo_version}
Requires: libgnomecanvas-devel >= %{libgnomecanvas_version}
Requires: libgnome-devel >= %{libgnome_version}
Requires: libart_lgpl-devel >= %{libart_lgpl_version}
Requires: gtk2-devel >= %{gtk2_version}
Requires: libglade2-devel >= %{libglade2_version}
Conflicts: bonobo-devel < 1.0.8

%description devel

Bonobo is a component system based on CORBA, used by the GNOME desktop.
libbonoboui contains GUI components that come with Bonobo.

This package contains header files used to compile programs that 
use libbonoboui.

%prep
%setup -q -n %{name}-%{version}
# intltool 0.13 wants NDBM_File, which we don't include 
intltoolize --force --copy

%build

rm ltmain.sh && cp %{SOURCE2} ltmain.sh
for i in config.guess config.sub ; do
	test -f /usr/share/libtool/$i && cp /usr/share/libtool/$i .
done

%configure 

make ## %{?_smp_mflags} 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)

%doc AUTHORS COPYING ChangeLog NEWS README

%{_libdir}/lib*.so.*
%{_libdir}/libglade/2.0/*
%{_libdir}/bonobo
%{_datadir}/gnome-2.0

%files devel
%defattr(-,root,root)

%{_libdir}/lib*.a
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_bindir}/*

%changelog
* Wed Jan 30 2002 Owen Taylor <otaylor@redhat.com>
- Version 1.110.0
- Reintoolize to fix DBM problems

* Mon Jan 28 2002 Havoc Pennington <hp@redhat.com>
- rebuild in rawhide

* Mon Jan  7 2002 Havoc Pennington <hp@redhat.com>
- 1.108.1.90 cvs snap

* Tue Nov 27 2001 Havoc Pennington <hp@redhat.com>
- 1.107.0.90 snap, explicit requires lines for dependencies
- add libtool hack to avoid relinking

* Mon Oct 29 2001 Havoc Pennington <hp@redhat.com>
- add glade dependency, add glade module to file list

* Sun Oct 28 2001 Havoc Pennington <hp@redhat.com>
- rebuild with glib 1.3.10, new cvs snap

* Mon Oct 15 2001 Havoc Pennington <hp@redhat.com>
- rebuild, hoping build root is fixed

* Mon Oct 15 2001 Havoc Pennington <hp@redhat.com>
- grumble, build require newer gtk
- require libart_lgpl-devel not the non-devel package

* Mon Oct 15 2001 Havoc Pennington <hp@redhat.com>
- cvs snap with menu stuff fixed so gnome-terminal works

* Fri Oct  5 2001 Havoc Pennington <hp@redhat.com>
- new tarball, rebuild for new glib

* Mon Sep 24 2001 Havoc Pennington <hp@redhat.com>
- new cvs snap, fix up prereqs/requires a bit

* Tue Sep 18 2001 Havoc Pennington <hp@redhat.com>
- Initial build.
