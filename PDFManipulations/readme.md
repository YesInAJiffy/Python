# Compression of PDF Files

## Windows
1. Download and install
https://ghostscript.com/releases/gsdnld.html
2. Ensure that the path is set OR go to the bin directory and run the gs command
3. Path to set
   C:\Program Files\gs\gs9.50\bin
## Mac
brew install ghostscript
## Ubuntu
sudo apt install ghostscript
## Validate installation
Check version to verify installation is successful
gs --version


# Compression Command
```console
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook -dNOPAUSE -dBATCH -sOutputFile=output.pdf input.pdf
```

## Important Option (which sets the compression)
/screen: Low-resolution, smaller file size. <br>
/ebook: Medium-resolution, smaller than print quality but better than screen.<br>
/printer: Higher quality suitable for printing.<br>
/prepress: High quality for prepress and printing.<br>
/default: A balance between size and quality.<br>
## Complete listing of options
-sDEVICE=pdfwrite: Specifies that the output device is PDF.<br>
-dCompatibilityLevel=1.4: Sets the PDF version.<br>
-dPDFSETTINGS=/screen: This setting is for low-resolution output, suitable for screen viewing. You can choose other settings as well:<br>
/screen: Low-resolution, smaller file size.<br>
/ebook: Medium-resolution, smaller than print quality but better than screen.<br>
/printer: Higher quality suitable for printing.<br>
/prepress: High quality for prepress and printing.<br>
/default: A balance between size and quality.<br>
-dNOPAUSE: Prevents Ghostscript from prompting after each page.<br>
-dBATCH: Exits after processing.<br>
output.pdf: The name of the reduced-size output file.<br>
input.pdf: The name of the input PDF file.<br>
