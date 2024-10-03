import csv
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics
from .serializers import CSVDataSerializer
from .models import CSVData

@api_view(['POST'])
def upload_csv(request):
    try:
        # Verificar se um arquivo foi enviado
        csv_file = request.FILES.get('file')
        if not csv_file:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        # Ler o conteúdo do arquivo CSV enviado
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        
        # Remover o BOM se presente
        if decoded_file[0].startswith('\ufeff'):
            decoded_file[0] = decoded_file[0][len('\ufeff'):]

        # Definir o delimitador como ponto e vírgula
        reader = csv.DictReader(decoded_file, delimiter=';')

        # Log para ver as colunas do CSV
        print("Colunas do CSV:", reader.fieldnames)

        # Processar cada linha e salvar no banco de dados
        for row in reader:
            # Verificar se as colunas esperadas estão presentes
            if 'SUBSTANCIA' in row and 'CNPJ' in row and 'LABORATORIO' in row:
                CSVData.objects.create(
                    SUBSTANCIA=row['SUBSTANCIA'],
                    CNPJ=row['CNPJ'],
                    LABORATORIO=row['LABORATORIO']
                )
            else:
                return Response({'error': 'Invalid CSV format'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'CSV processed successfully!'}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CSVDataListView(generics.ListAPIView):
    queryset = CSVData.objects.all()
    serializer_class = CSVDataSerializer
