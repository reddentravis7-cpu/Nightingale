$root = "C:\nightingale"
$dest = Join-Path $root "04_Translate"

$folders = @(
    "knowledge\cisco-ios",
    "knowledge\hl7-fhir",
    "knowledge\acl-top-350",
    "knowledge\ge-oec-one-cfd",
    "docs\architecture",
    "docs\decisions",
    "docs\guides\handoffs",
    "tools",
    "services"
)

foreach ($f in $folders) {
    $path = Join-Path $dest $f
    New-Item -ItemType Directory -Force -Path $path | Out-Null
}

Write-Host "Created 04_Translate engineering subtree." -ForegroundColor Green

$ciscoSrc = Join-Path $root "01_Networking\Cisco_IOS"
$ciscoDst = Join-Path $dest "knowledge\cisco-ios"
if (Test-Path $ciscoSrc) {
    Copy-Item -Path (Join-Path $ciscoSrc "*") -Destination $ciscoDst -Recurse -Force
    Write-Host "Copied real Cisco content from $ciscoSrc to $ciscoDst" -ForegroundColor Green
} else {
    Write-Host "WARNING: $ciscoSrc not found, skipped." -ForegroundColor Yellow
}

$hl7Src = Join-Path $root "03_Clinical_Integration\HL7"
$hl7Dst = Join-Path $dest "knowledge\hl7-fhir"
if (Test-Path $hl7Src) {
    Copy-Item -Path (Join-Path $hl7Src "*") -Destination $hl7Dst -Recurse -Force
    Write-Host "Copied real HL7 content from $hl7Src to $hl7Dst" -ForegroundColor Green
} else {
    Write-Host "WARNING: $hl7Src not found, skipped." -ForegroundColor Yellow
}

$aclSrc = Join-Path $root "knowledge\acl-top-350"
$aclDst = Join-Path $dest "knowledge\acl-top-350"
if (Test-Path $aclSrc) {
    Copy-Item -Path (Join-Path $aclSrc "*") -Destination $aclDst -Recurse -Force
    Write-Host "Copied ACL TOP 350 placeholder content." -ForegroundColor Green
}

$geSrc = Join-Path $root "knowledge\ge-oec-one-cfd"
$geDst = Join-Path $dest "knowledge\ge-oec-one-cfd"
if (Test-Path $geSrc) {
    Copy-Item -Path (Join-Path $geSrc "*") -Destination $geDst -Recurse -Force
    Write-Host "Copied GE OEC placeholder content." -ForegroundColor Green
}

$pairs = @{
    "docs"     = "docs"
    "tools"    = "tools"
    "services" = "services"
}
foreach ($k in $pairs.Keys) {
    $src = Join-Path $root $k
    $dst = Join-Path $dest $pairs[$k]
    if (Test-Path $src) {
        Copy-Item -Path (Join-Path $src "*") -Destination $dst -Recurse -Force
        Write-Host "Copied $src into $dst" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "=== DONE COPYING. NOTHING DELETED. ===" -ForegroundColor Cyan
Write-Host "Manually verify 04_Translate content, then decide what to remove from:" -ForegroundColor Cyan
Write-Host "  - $root\01_Networking\Cisco_IOS (now duplicated in 04_Translate)"
Write-Host "  - $root\03_Clinical_Integration\HL7 (now duplicated in 04_Translate)"
Write-Host "  - $root\knowledge\cisco-ios and knowledge\hl7-fhir (stale, superseded)"
Write-Host "  - $root\knowledge\acl-top-350 and knowledge\ge-oec-one-cfd (now duplicated)"
Write-Host "  - $root\docs, $root\tools, $root\services (now duplicated)"