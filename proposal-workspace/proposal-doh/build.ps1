$ErrorActionPreference = 'Stop'
$texLiveBin = 'C:\texlive\2026\bin\windows'
$xeLatex = Join-Path $texLiveBin 'xelatex.exe'
$pdfInfo = Join-Path $texLiveBin 'pdfinfo.exe'

if (-not (Test-Path -LiteralPath $xeLatex)) {
    throw "TeX Live xelatex not found at $xeLatex"
}
if (-not (Test-Path -LiteralPath $pdfInfo)) {
    throw "TeX Live pdfinfo not found at $pdfInfo"
}

for ($pass = 1; $pass -le 2; $pass++) {
    & $xeLatex -interaction=nonstopmode -halt-on-error main.tex
    if ($LASTEXITCODE -ne 0) {
        throw "LaTeX build failed on pass $pass with exit code $LASTEXITCODE"
    }
}

$pageLine = & $pdfInfo main.pdf | Select-String '^Pages:\s+(\d+)'
if (-not $pageLine) {
    throw 'Could not read PDF page count'
}

$pages = [int]$pageLine.Matches[0].Groups[1].Value
if ($pages -ne 2) {
    throw "Expected exactly 2 pages, got $pages"
}

Write-Host "Build complete: main.pdf ($pages pages)"
