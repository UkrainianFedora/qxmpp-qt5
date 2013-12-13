Name:       qxmpp
Version:    0.7.5
Release:    3%{?dist}
License:    LGPLv2+

Source0:    http://qxmpp.googlecode.com/files/qxmpp-0.7.5.tar.gz
Obsoletes:  qxmpp-dev < 0.7.5
Provides:   qxmpp-dev = %{version}-%{release}

Patch1:     qxmpp-dynamiclib.patch

Summary:    Qt XMPP Library
URL:        http://code.google.com/p/qxmpp/

BuildRequires:  qt4-devel
BuildRequires:  speex-devel

%description
QXmpp is a cross-platform C++ XMPP client library. It is based on Qt and C++.

QXmpp is pretty intuitive and easy to use. It uses Qt extensively. Qt is the only
third party library it is dependent on. Users need to a have working knowledge of
C++ and Qt basics (Signals and Slots and Qt data types). The underlying TCP socket
and the XMPP RFCs (RFC3920 and RFC3921) have been encapsulated into classes and
functions. Therefore the user would not be bothered with these details. But it is
always recommended to the advanced users to read and enjoy the low level details.

%package devel
Summary:      QXmpp Development Files
Requires:     %{name}%{?_isa} = %{version}-%{release}
Obsoletes: qxmpp-dev-devel < 0.7.5 
Provides:  qxmpp-dev-devel = %{version}-%{release}

%description devel
It's a development package for qxmpp-dev.

QXmpp is a cross-platform C++ XMPP client library. It is based on Qt and C++.

%prep
%setup -q
%patch1 -p1

%build
%{_qt4_qmake} PREFIX=%{_prefix} LIBDIR=%{_lib} QMAKE_STRIP="" QMAKE_CXXFLAGS+="%{optflags}"
make %{?_smp_mflags}

%install
%make_install INSTALL_ROOT=${RPM_BUILD_ROOT}

# move installed docs to include them in -devel package via %%doc magic
rm -rf __tmp_doc ; mkdir __tmp_doc
mv ${RPM_BUILD_ROOT}%{_docdir}/%{name}/* __tmp_doc

%post -n %{name} -p /sbin/ldconfig
%postun -n %{name} -p /sbin/ldconfig

%files 
%doc AUTHORS CHANGELOG LICENSE.LGPL README
%{_libdir}/libqxmpp.so.0
%{_libdir}/libqxmpp.so.0.7
%{_libdir}/libqxmpp.so.0.7.5

%files devel
%doc __tmp_doc/*
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Fri Dec 13 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 0.7.5-3
- Fix duplicate documentation (#1001295)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Minh Ngo <nlminhtl@gmail.com> 0.7.5-1
- new version

* Fri Nov 09 2012 Minh Ngo <nlminhtl@gmail.com> 0.7.4-1
- new version

* Sun Sep 30 2012 Minh Ngo <nlminhtl@gmail.com> 0.7.3-4
- Upd. to the last version for leechcraft IC compatibility.

* Wed Sep 26 2012 Minh Ngo <nlminhtl@gmail.com> 0.7.3-2
- Adding obsoletes

* Tue Sep 11 2012 Minh Ngo <nlminhtl@gmail.com> 0.7.3-1
- Renaming package name. Merging code bases between qxmpp-dev and qxmpp.

* Sat Aug 11 2012 Minh Ngo <nlminhtl@gmail.com> 0.6.3.1-1
- Updating to the new version
- Changelog https://raw.github.com/0xd34df00d/qxmpp-dev/master/CHANGELOG

* Thu Apr 26 2012 Minh Ngo <nlminhtl@gmail.com> 0.3.61-1
- XEP 0033

* Sat Mar 17 2012 Minh Ngo <nlminhtl@gmail.com> 0.3.47-1
- Synchronization with upstream
- updating patches

* Wed Mar 14 2012 Minh Ngo <nlminhtl@gmail.com> 0.3.45.2-1
- Synchronization with upstream

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.45.1-6
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.45.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jan 08 2012 Minh Ngo <nlminhtl@gmail.com> 0.3.45.1-4
- fixing summary/description in the devel package
- adding a dependence for the devel package

* Fri Nov 11 2011 Minh Ngo <nlminhtl@gmail.com> 0.3.45.1-3
- rename the lib to libqxmpp-dev

* Tue Aug 02 2011 Minh Ngo <nlminhtl@gmail.com> 0.3.45.1-2
- dynamic libs

* Mon Jul 25 2011 Minh Ngo <nlminhtl@gmail.com> 0.3.45.1-1
- new version

* Mon Jun 06 2011 Minh Ngo <nlminhtl@gmail.com> 0.3.44-0.1.pre21062011
- initial build 
