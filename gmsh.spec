Summary:	A 3D mesh generator with pre- and post-processing facilities
Summary(pl):	Generator siatki 3D zawieraj±cy pre/post procesor
Name:		gmsh
Version:	1.61.3
Release:	0.1
License:	GPL
Group:		Applications/Engineering
Source0:	http://www.geuz.org/gmsh/src/%{name}-%{version}-source.tgz
# Source0-md5:	1cb5d61bd6a150b1bc4b372e869a6f20
Source1:	%{name}.desktop
URL:		http://www.geuz.org/gmsh/
BuildRequires:	autoconf
BuildRequires:	OpenGL-devel
BuildRequires:	fltk-gl-devel >= 1.1.0
BuildRequires:	gsl-devel >= 1.2
BuildRequires:	texinfo-texi2dvi
BuildRequires:	tetex-dvips
BuildRequires:	tetex-format-plain
BuildRequires:	tetex-format-pdftex
Requires:	getdp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gmsh is an automatic three-dimensional finite element mesh generator,
primarily Delaunay, with built-in pre- and post-processing facilities.
Its primal design goal is to provide a simple meshing tool for
academic test cases with parametric input and up to date visualization
capabilities. One of the strengths of Gmsh is its ability to respect a
characteristic length field for the generation of adapted meshes on
lines, surfaces and volumes. Gmsh requires OpenGL (or Mesa) to be
installed on your system.

%description -l pl
Gmsh jest automatycznym generatorem trójwymiarowej siatki elementów
skoñczonych (g³ównie Delaunay), z wbudowanym pre/post procesorem.
G³ównym zadaniem przy projektowaniu Gmsh by³o stworzenie prostego
narzêdzia wykorzystywanego w testach akademickich, do generowania
siatki, z parametrycznym wej¶ciem i mo¿liwo¶ci± wizualizacji wyników
na bie¿±co. Jedn± z mocnych stron Gmesh jest mo¿liwo¶æ okre¶lenia
d³ugo¶ci generowanego elementu, która zostanie zastosowana do
dyskretyzacji linii, powierzchni i objêto¶ci. Gmesh wymaga OpenGL (lub
Mesy) zainstalowanej w twoim systemie.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}
%{__make} utils
%{__make} doc
%{__make} doc-info

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_infodir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_pixmapsdir}

install bin/{gmsh,dxf2geo} $RPM_BUILD_ROOT%{_bindir}
install doc/gmsh.1 $RPM_BUILD_ROOT%{_mandir}/man1
install doc/texinfo/gmsh.info* $RPM_BUILD_ROOT%{_infodir}
install utils/icons/gmsh48x48.png $RPM_BUILD_ROOT%{_pixmapsdir}/gmsh.png

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO doc/{CREDITS,FAQ,VERSIONS}
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_infodir}/*.info*
%{_mandir}/man1/*
%{_pixmapsdir}/%{name}.png
