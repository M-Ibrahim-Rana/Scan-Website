from osgeo import gdal
print("yo")

# Open the GeoTIFF file
dataset = gdal.Open("ndvi.tif")
print("yo")

# Get the geotransform of the image
geotransform = dataset.GetGeoTransform()
print("yo")

# The geotransform is an array of 6 values: (TopLeftX, PixelSizeX, Rotation, TopLeftY, Rotation, PixelSizeY)
# Extract the coordinates of the top-left and bottom-right corners
top_left_x = geotransform[0]
top_left_y = geotransform[3]
pixel_size_x = geotransform[1]
pixel_size_y = geotransform[5]
print("yo")

# Get the image dimensions (number of columns and rows)
cols = dataset.RasterXSize
rows = dataset.RasterYSize
print("yo")

# Calculate the coordinates of the bottom-right corner
bottom_right_x = top_left_x + (cols * pixel_size_x)
bottom_right_y = top_left_y + (rows * pixel_size_y)

print("yo")
# Print the bounds (top-left and bottom-right coordinates)
print(f"Top-left corner: ({top_left_x}, {top_left_y})")
print(f"Bottom-right corner: ({bottom_right_x}, {bottom_right_y})")
