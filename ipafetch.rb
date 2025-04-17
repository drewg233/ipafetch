class Ipafetch < Formula
  include Language::Python::Virtualenv

  desc "A tool to fetch IPA files from Apple Configurator"
  homepage "https://github.com/drewg233/ipafetch"
  url "https://files.pythonhosted.org/packages/source/i/ipafetch/ipafetch-0.1.0.tar.gz"
  sha256 "" # You'll need to fill this in after uploading to PyPI
  license "MIT"

  depends_on "python@3.6"

  def install
    virtualenv_install_with_resources
  end

  test do
    system "#{bin}/ipafetch", "--help"
  end
end 