# revision 19886
# category Package
# catalog-ctan /macros/latex/contrib/gatech-thesis
# catalog-date 2010-07-26 16:46:28 +0200
# catalog-license gpl
# catalog-version 1.8
Name:		texlive-gatech-thesis
Version:	1.8
Release:	2
Summary:	Georgia Institute of Technology thesis class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gatech-thesis
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gatech-thesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gatech-thesis.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The output generated by using this class has been approved by
the Georgia Tech Office of Graduate Studies. It satisfies their
undocumented moving-target requirements in additional to the
actual documented requirements of the June 2002 Georgia Tech
Thesis Style Manual, as amended up to 2010.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/gatech-thesis/gatech-thesis-losa.bst
%{_texmfdistdir}/bibtex/bst/gatech-thesis/gatech-thesis.bst
%{_texmfdistdir}/makeindex/gatech-thesis/gatech-thesis-index.ist
%{_texmfdistdir}/tex/latex/gatech-thesis/gatech-thesis-gloss.sty
%{_texmfdistdir}/tex/latex/gatech-thesis/gatech-thesis-index.sty
%{_texmfdistdir}/tex/latex/gatech-thesis/gatech-thesis-losa.sty
%{_texmfdistdir}/tex/latex/gatech-thesis/gatech-thesis-patch.sty
%{_texmfdistdir}/tex/latex/gatech-thesis/gatech-thesis.cls
%doc %{_texmfdistdir}/doc/latex/gatech-thesis/CHANGES
%doc %{_texmfdistdir}/doc/latex/gatech-thesis/COMPLIANCE
%doc %{_texmfdistdir}/doc/latex/gatech-thesis/COPYING
%doc %{_texmfdistdir}/doc/latex/gatech-thesis/ChangeLog
%doc %{_texmfdistdir}/doc/latex/gatech-thesis/INSTALL
%doc %{_texmfdistdir}/doc/latex/gatech-thesis/MANIFEST
%doc %{_texmfdistdir}/doc/latex/gatech-thesis/NEWS
%doc %{_texmfdistdir}/doc/latex/gatech-thesis/NOTES
%doc %{_texmfdistdir}/doc/latex/gatech-thesis/README
%doc %{_texmfdistdir}/doc/latex/gatech-thesis/TODO
%doc %{_texmfdistdir}/doc/latex/gatech-thesis/example-thesis.bib
%doc %{_texmfdistdir}/doc/latex/gatech-thesis/example-thesis.pdf
%doc %{_texmfdistdir}/doc/latex/gatech-thesis/example-thesis.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex makeindex tex doc %{buildroot}%{_texmfdistdir}
