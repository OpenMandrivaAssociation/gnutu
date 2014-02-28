%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Student's Schedule
Name:		gnutu
Version:	2.5
Release:	6
License:	GPLv2+
Group:		Education
Url:		http://www.gnutu.devnull.pl/
Source0:	http://gnutu.devnull.pl/download.php?id=sources/gnutu-%{version}.tar.gz
Patch0:		%{name}-desktop.patch
BuildRequires:	gtk-sharp2
BuildRequires:	glade-sharp2
BuildRequires:	pkgconfig(mono)

%description
GNUTU (Student's Schedule) is designed for students from primary and secondary
schools - using it, you can note various information (like marks, tests' dates
and important school events). It also can create various statistics, search
for all entered data, calculate your average; it can also serve as a diary and
many, many more...

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*
%{_datadir}/applications/gnutu.desktop
%{_datadir}/pixmaps/gnutu.ico
%{_datadir}/pixmaps/gnutu.png

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1 -b .%{name}-desktop.patch

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

