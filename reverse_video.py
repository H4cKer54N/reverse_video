import cv2
import argparse
from multiprocessing import Pool

class InvertirVideo:
        
    @staticmethod
    def invert_frame(frame):
        frame_invertido = cv2.flip(frame, 0)
        return frame_invertido

    @staticmethod
    def invert_video(nombre_video, nombre_salida=None, calidad=100, num_procesos=2):
        # Código para invertir el video utilizando multiprocessing

        video = cv2.VideoCapture(nombre_video)
        
        # Obtener información del video
        fps = video.get(cv2.CAP_PROP_FPS)
        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        ancho = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        alto = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

        if nombre_salida:
            # Crear un objeto para escribir el nuevo video invertido
            codec = cv2.VideoWriter_fourcc(*'mp4v')
            nuevo_video = cv2.VideoWriter(nombre_salida, codec, fps, (ancho, alto), isColor=True)

        pool = Pool(processes=num_procesos)

        # Leer los fotogramas del video original y aplicar procesamiento en paralelo
        for i in range(total_frames - 1, -1, -1):
            video.set(cv2.CAP_PROP_POS_FRAMES, i)
            ret, frame = video.read()
            if ret:
                if calidad < 100:
                    ancho_reducido = int(ancho * calidad / 100)
                    alto_reducido = int(alto * calidad / 100)
                    frame = cv2.resize(frame, (ancho_reducido, alto_reducido), interpolation=cv2.INTER_LINEAR)

                frame_invertido = pool.apply_async(InvertirVideo.invert_frame, (frame,)).get()

                if nombre_salida:
                    nuevo_video.write(frame_invertido)
                
                if nombre_salida is None:
                    cv2.imshow("Video invertido", frame_invertido)

                progreso = int((i + 1) / total_frames * 100)
                print(f"Procesando: {progreso}% completado", end='\r')

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        video.release()
        if nombre_salida:
            nuevo_video.release()
            print("El video se ha invertido correctamente. Se ha guardado como", nombre_salida)
        else:
            cv2.destroyAllWindows()

def main():
    parser = argparse.ArgumentParser(description='Programa para invertir videos.')
    parser.add_argument('--v', '--video', required=True, help='Ruta y nombre del video de entrada')
    parser.add_argument('--vo', '--videooutput', help='Ruta y nombre del video de salida (opcional)')
    parser.add_argument('--q', '--qualita', type=int, default=100, help='Porcentaje de calidad del video de salida (valor entero entre 0 y 100, por defecto 100)')
    parser.add_argument('--np', '--numprocesos', type=int, default=2, help='Número de procesos a utilizar para el procesamiento en paralelo (valor entero, por defecto 2)')

    args = parser.parse_args()

    if args.vo:
        InvertirVideo.invert_video(args.v, args.vo, args.q, args.np)
    else:
        InvertirVideo.invert_video(args.v, calidad=args.q, num_procesos=args.np)

if __name__ == "__main__":
    main()
