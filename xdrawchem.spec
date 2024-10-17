%define name xdrawchem
%define version 1.9.9
%define release %mkrel 7

Summary: 	2D chemical structures drawing tool
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	xdrawchem-%{version}.tar.bz2
Patch0:		%{name}-gcc43.patch
Patch1:		%{name}-ob22.patch
Patch2:		xdrawchem-warn.patch
URL: 		https://xdrawchem.sourceforge.net
License: 	GPLv2+
Group: 		Sciences/Chemistry
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires: 	qt3-devel openbabel-devel >= 2.0.0
Requires:	openbabel >= 2.0.0
Obsoletes:	kde3-xdrawchem
Provides:	kde3-xdrawchem

%description
XDrawChem is a two-dimensional molecule drawing program for Unix
operating systems.  It is similar in functionality to other molecule
drawing programs such as ChemDraw (TM, CambridgeSoft).  It can read
and write MDL Molfiles and CML files to allow sharing between
XDrawChem and other chemistry applications.

%prep
%setup -q
%patch0 -p1 -b .gcc43
%patch1 -p1 -b .ob
%patch2 -p1 -b .warn

%build
export PATH="%qt3bin:$PATH"
%configure2_5x \
	--with-qtincdir=%qt3include \
	--with-qtlibdir=%qt3lib
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

install -Dpm 644 ring/xdrawchem-icon.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/xdrawchem.png

# menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=XDrawChem
Comment=2D chemical structure editor
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Science;Chemistry;Qt;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%update_menus
%endif


%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc COPYRIGHT.txt GPL.txt HISTORY.txt INSTALL.txt README.txt
%doc TODO.txt 
%_bindir/xdrawchem
%dir %_datadir/xdrawchem
%_datadir/xdrawchem/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/xdrawchem.png
