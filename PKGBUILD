pkgname=nvmesmart
pkgver=0.1
pkgrel=1
pkgdesc="a easy cli and maybe gui smart tool for linux"
arch=('any')
url="https://github.com/ingressy/nvmesmart/"
license=('MIT')
depends=('python' 'smartmontools')  # Ersetze 'python-paketname' durch benötigte Abhängigkeiten
source=("$pkgname-$pkgver.tar.gz::https://github.com/ingressy/nvmesmart/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('SKIP')  # Alternativ den tatsächlichen SHA256-Wert der Datei angeben

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python main.py install --root="$pkgdir/" --optimize=1
}
