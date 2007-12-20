Summary:	A 3D mesh generator with pre- and post-processing facilities
Summary(pl.UTF-8):	Generator siatki 3D zawierający pre/post procesor
Name:		gmsh
Version:	2.0.8
Release:	0.1
License:	GPL
Group:		Applications/Engineering
Source0:	http://www.geuz.org/gmsh/src/%{name}-%{version}-source.tgz
# Source0-md5:	123e7f40dedcc0f2ec33ff1af4b8d127
Source1:	%{name}.desktop
Patch0:		%{name}-make-jN.patch
Patch1:		%{name}-link.patch
URL:		http://www.geuz.org/gmsh/
BuildRequires:	autoconf
BuildRequires:	OpenGL-GLU-devel
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

%description -l pl.UTF-8
Gmsh jest automatycznym generatorem trójwymiarowej siatki elementów
skończonych (głównie Delaunay), z wbudowanym pre/post procesorem.
Głównym zadaniem przy projektowaniu Gmsh było stworzenie prostego
narzędzia wykorzystywanego w testach akademickich, do generowania
siatki, z parametrycznym wejściem i możliwością wizualizacji wyników
na bieżąco. Jedną z mocnych stron Gmesh jest możliwość określenia
długości generowanego elementu, która zostanie zastosowana do
dyskretyzacji linii, powierzchni i objętości. Gmesh wymaga OpenGL (lub
Mesy) zainstalowanej w twoim systemie.

%prep
%setup -q
%patch0 -p1

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
%doc README doc/{CREDITS,FAQ,TODO,VERSIONS}
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_infodir}/*.info*
%{_mandir}/man1/*
%{_pixmapsdir}/%{name}.png
