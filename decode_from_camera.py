# import cv2
# import decode from pyzbar to decode the barcode
import cv2
from pyzbar.pyzbar import decode


# Function to scan barcodes using the webcam
def scan_barcodes():
    cap = cv2.VideoCapture(1)  # 0 corresponds to the built-in webcam

    while True:
        ret, frame = cap.read()

        if not ret:
            continues

        barcodes = decode(frame)

        for barcode in barcodes:
            barcode_data = barcode.data.decode('utf-8')
            barcode_type = barcode.type

            # Display the barcode data and type on the frame
            cv2.putText(frame, f'Type: {barcode_type}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.putText(frame, f'Data: {barcode_data}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        cv2.imshow("Barcode Scanner", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' key to exit
            cap.release()
            cv2.destroyAllWindows()
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    scan_barcodes()
