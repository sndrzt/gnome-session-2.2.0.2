%define __spec_install_post /usr/lib/rpm/brp-compress
Summary:          The gnome desktop programs for the GNOME GUI desktop environment.
Name:             gnome-session
Version:          2.2.0.2
Release:          1
License:          LGPL
Group:            System Environment/Base
Source:           %{name}-%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-root
URL:              http://www.gnome.org
BuildRequires:    pkgconfig >= 0.8
Requires:         libgnomecanvas >= @LIBGNOMECANVAS_REQUIRED@
Requires:         libgnomeui >= 2.0.0
BuildRequires:    libgnomecanvas-devel >= @LIBGNOMECANVAS_REQUIRED@
BuildRequires:    libgnomeui-devel >= 2.0.0

%description
GNOME (GNU Network Object Model Environment) is a user-friendly
set of applications and desktop tools to be used in conjunction with a
window manager for the X Window System.  GNOME is similar in purpose and
scope to CDE and KDE, but GNOME is based completely on free
software.  The gnome-core package includes the basic programs and
libraries that are needed to install GNOME.

GNOME session provides the session tools for the the gnome desktop.

%package devel
Summary:          GNOME desktop session tools and includes.
Group:            Development/Libraries
Requires:         %name = %version
Requires:         pkgconfig >= 0.8
Requires:         libgnomecanvas >= @LIBGNOMECANVAS_REQUIRED@
Requires:         libgnomecanvas-devel >= @LIBGNOMECANVAS_REQUIRED@
Requires:         libgnomeui >= 2.0.0
Requires:         libgnomeui-devel >= 2.0.0

%description devel
Session libraries and header files for creating GNOME sessions.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT


export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%makeinstall

unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

%find_lang %{name}-2.0

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files -f %{name}-2.0.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%defattr (-, root, root)
%{_bindir}/*
%{_mandir}/man5/*
# %{_datadir}/control-center/capplets/*
%{_datadir}/control-center/Session/*
%{_datadir}/gnome/*
%{_datadir}/omf
%{_datadir}/pixmaps
%{_datadir}/control-center-2/capplets/
%{_mandir}/man1/*

%changelog
* Tue Mar 05 2002 Chris Chabot <chabotc@reviewboard.com>
- Final cleanups
- make .spec.in

* Sun Feb 15 2002 Chris Chabot <chabotc@reviewboard.com>
- initial spec file for gnome-session
