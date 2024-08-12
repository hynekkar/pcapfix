Name:           pcapfix
Version:        1.1.0
Release:        8%{?dist}
Summary:        A tool for repairing corrupted pcap files
License:        GPLv3
URL:            http://f00l.de/pcapfix
Source0:        pcapfix-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-XXXXXX)
Provides: pcapfix
Requires: libpcap
 
BuildRequires: gcc
BuildRequires: make
 
%description
pcapfix is a repair tool for corrupted pcap files. It checks for an intact pcap
global header and repairs it if there are any corrupted bytes. If one is not
present, one is created and added to the beginning of the file. It then tries
to find pcap packet headers, and checks and repairs them.
 
%prep
%setup -q
sed -i 's|install -D|install -pD|g' Makefile
 
%build
# Upstream has used -Wl,-z,relro.
make all
#%make_build DEBUGFLAGS+="%{optflags}"
 
%install
%make_install
%files
%doc Changelog README
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
 
%changelog
* Sun Feb 18 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 1.1.0-8
- Add gcc and make as BR (minimal buildroot change)
 
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
 
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
 
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
 
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
 
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
 
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
 
* Mon Feb 09 2015 Christopher Meng <rpm@cicku.me> - 1.1.0-1
- Update to 1.1.0
 
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
 
* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
 
* Mon Nov 04 2013 Christopher Meng <rpm@cicku.me> - 1.0.1-1
- Update to 1.0.1
 
* Mon Oct 14 2013 Christopher Meng <rpm@cicku.me> - 1.0.0-1
- New version.
 
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
 
* Mon Jul 22 2013 Christopher Meng <rpm@cicku.me> - 0.7.3-2
- Fix incorrect license.
 
* Tue Jun 18 2013 Christopher Meng <rpm@cicku.me> - 0.7.3-1
- Initial package.
