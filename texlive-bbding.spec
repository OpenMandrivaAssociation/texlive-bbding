%global tl_name bbding
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.01
Release:	%{tl_revision}.1
Summary:	A symbol (dingbat) font and LaTeX macros for its use
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/bbding
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bbding.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bbding.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bbding.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A symbol font (distributed as Metafont source) that contains many of the
symbols of the Zapf dingbats set, together with an NFSS interface for
using the font. An Adobe Type 1 version of the fonts is available in the
niceframe fonts bundle.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/fonts/source
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bbding
%dir %{_datadir}/texmf-dist/fonts/source/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/source/latex/bbding
%dir %{_datadir}/texmf-dist/tex/latex/bbding
%dir %{_datadir}/texmf-dist/fonts/source/public/bbding
%dir %{_datadir}/texmf-dist/fonts/tfm/public/bbding
%doc %{_datadir}/texmf-dist/doc/latex/bbding/README
%doc %{_datadir}/texmf-dist/doc/latex/bbding/bbding.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bbding/bbding10.org
%doc %{_datadir}/texmf-dist/fonts/source/public/bbding/bbding10.mf
%{_datadir}/texmf-dist/fonts/tfm/public/bbding/bbding10.tfm
%doc %{_datadir}/texmf-dist/source/latex/bbding/bbding.dtx
%doc %{_datadir}/texmf-dist/source/latex/bbding/bbding.ins
%{_datadir}/texmf-dist/tex/latex/bbding/Uding.fd
%{_datadir}/texmf-dist/tex/latex/bbding/bbding.sty
