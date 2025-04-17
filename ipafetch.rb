class Ipafetch < Formula
  desc "A tool to fetch IPA files from Apple Configurator"
  homepage "https://github.com/drewg233/ipafetch"
  url "https://github.com/drewg233/ipafetch.git"
  version "0.1.0"
  license "MIT"

  depends_on "python@3.6"

  def install
    # Install the Python script
    bin.install "ipafetch/ipafetch.py" => "ipafetch"
    # Make the script executable
    chmod 0755, bin/"ipafetch"
  end

  test do
    system "#{bin}/ipafetch", "--help"
  end
end 