from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH

print('Contratante:')
contratante_nome = input('Nome: ')
contratante_rua = input('Rua e número: ')
contratante_cidade = input('Cidade: ')
contratante_id = input('Identificação: ')

print()
print('Contratado:')
contratado_nome = input('Nome: ')
contratado_rua = input('Rua e número: ')
contratado_cidade = input('Cidade: ')
contratado_id = input('Identificação: ')

documento = Document()
titulo_principal = documento.add_heading('Contrato de Prestação de Serviços', level=0).paragraph_format
titulo_principal.alignment = WD_ALIGN_PARAGRAPH.CENTER


titulo = documento.add_heading('Identificação das partes contratantes', level=1).paragraph_format
titulo.alignment = WD_ALIGN_PARAGRAPH.CENTER
documento.add_paragraph('')


paragrafo1 = documento.add_paragraph('')
r1 = paragrafo1.add_run('Contratante: ').bold = True
paragrafo1.add_run(f'{contratante_nome}, com sede em {contratante_rua} ({contratante_cidade}), inscrito sob o nº {contratante_id}.')
documento.add_paragraph('')


paragrafo2 = documento.add_paragraph('')
r2 = paragrafo2.add_run('Contratado: ').bold = True
paragrafo2.add_run(f'{contratado_nome}, com sede em {contratado_rua} ({contratado_cidade}), inscrito sob o nº {contratado_id}.')


paragrafo3 = documento.add_paragraph('2. CLÁUSULA SEGUNDA - DO REGIME DE EXECUÇÃO\
2.1. O serviço contratado será realizado por execução indireta, sob o regime de empreitada\
por menor preço global.\
3. CLÁUSULA TERCEIRA – DA FORMA DE PRESTAÇÃO DO SERVIÇO\
3.1. Será considerada como unidade de pagamento a lauda completa com 1.000 (mil)\
caracteres, eletronicamente contados pelo processador de textos no texto final, descontados\
os espaços em branco, para a quantificação dos trabalhos.\
3.2. O cálculo estimativo do número de laudas dar-se-á pelo uso do menu “ferramentas” e do.\
3.3.3. “REGIME URGENTÍSSIMO” - produção acima de 20,01 (vinte vírgula zero um) laudas.')

documento.add_paragraph('')
documento.add_paragraph('')
documento.add_paragraph('')
documento.add_paragraph('')

assinatura = documento.add_paragraph('')
assinatura.add_run('Assinatura ').bold = True
assinatura.add_run('_________________________________________________')
assinatura.alignment = WD_ALIGN_PARAGRAPH.CENTER

documento.save('contrato.docx')