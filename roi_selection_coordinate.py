
import cv2
import pytesseract



coordinates = [] 
  
# Defining the event listener (callback function)
def shape_selection(event, x, y, flags, param): 
    # making coordinates global
    global coordinates 
  
    # Storing the (x1,y1) coordinates when left mouse button is pressed  
    if event == cv2.EVENT_LBUTTONDOWN: 
        coordinates = [(x, y)] 
  
    # Storing the (x2,y2) coordinates when the left mouse button is released and make a rectangle on the selected region
    elif event == cv2.EVENT_LBUTTONUP: 
        coordinates.append((x, y)) 
  
        # Drawing a rectangle around the region of interest (roi)
        cv2.rectangle(image, coordinates[0], coordinates[1], (0,0,255), 2) 
        cv2.imshow("image", image) 
  
  
# load the image, clone it, and setup the mouse callback function 
image = cv2.imread(r'C:\Users\Ramesh\Desktop\Parsing_Project\Resumes_jpg\Akhil\output1.jpg')
image = cv2.resize(image,(800,740))
image_copy = image.copy()
cv2.namedWindow("image") 
cv2.setMouseCallback("image", shape_selection) 

f = open(r'C:\Users\Ramesh\Desktop\Parsing_Project\data.txt', "a")  
  
# keep looping until the 'q' key is pressed 
while True: 
    # display the image and wait for a keypress 
    cv2.imshow("image", image) 
    key = cv2.waitKey(1) & 0xFF
  
    if key==13:
        image_roi = image_copy[coordinates[0][1]:coordinates[1][1], 
                               coordinates[0][0]:coordinates[1][0]] 
        text = pytesseract.image_to_string(image_roi) 
        text = text.replace(',', ' ')
        print(text)
        f.write(text + '\n')    
    if key == ord("c"):
        
        image = image_copy.copy()   
    if key == ord("q"):
        f.close()
        
        break
    
    
  
if len(coordinates) == 2: 
    image_roi = image_copy[coordinates[0][1]:coordinates[1][1], 
                               coordinates[0][0]:coordinates[1][0]] 
    cv2.imshow("Selected Region of Interest - Press any key to proceed", image_roi) 
    cv2.waitKey(0) 

print(coordinates) 
# closing all open windows 
cv2.destroyAllWindows()  
