Summary:	Student's Schedule
Name:		gnutu
Version:	2.5
Release:	%mkrel 5
License:	GPL
Group:		Education
Source0:	http://gnutu.devnull.pl/download.php?id=sources/gnutu-%{version}.tar.gz
Patch0:		%{name}-desktop.patch
URL:		http://www.gnutu.devnull.pl/
BuildRequires:	gtk-sharp2
BuildRequires:	glade-sharp2
BuildRequires:	libmono-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
GNUTU (Student's Schedule) is designed for students 
from primary and secondary schools - using it, you 
can note various information (like marks, tests' dates 
and important school events). It also can create 
various statistics, search for all entered data, calculate 
your average; it can also serve as a diary and many, many more...

%prep
%setup -q %{name}-%{version}
%patch0 -p1 -b .%{name}-desktop.patch

%build

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}    

%makeinstall
    
%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif
    
%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}    

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*
%{_datadir}/applications/gnutu.desktop
%{_datadir}/pixmaps/gnutu.ico
%{_datadir}/pixmaps/gnutu.png
    



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.5-5mdv2010.0
+ Revision: 429287
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.5-4mdv2009.0
+ Revision: 246510
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2mdv2008.1-current
+ Revision: 136456
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Jan 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.5-2mdv2007.0
+ Revision: 110442
- correct url
- spec file clean

* Sat Jan 06 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.5-1mdv2007.1
+ Revision: 104707
- Import gnutu

