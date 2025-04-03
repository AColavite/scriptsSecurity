import java.nio.charset.StandardCharsets
import java.security.*
import java.util.*
import javax.crypto.*
import javax.crypto.spec.IvParameterSpec
import javax.crypto.spec.SecretKeySpec

object cryptoUtils {

    // Gerar key AES
    fun generateAESKey(): SecretKey{
        val keyGen = KeyGenerator.getInstance("AES")
        keyGen.init(256) //     AES
        return keyGen.generateKey()
    }

    // AES Encrypt
    fun decryptAES(encryptedText: String, secretKey: SecretKey): Pair<String, String> {
        val cipher = Cipher.getInstance("AES/CBC/PKCS5Padding")
        val iv = ByteArray(16)
        SecureRandom().nextBytes(iv)
        cipher.init(
            Cipher.DECRYPT_MODE, secretKey,
            IvParameterSpec(Base64.getDecoder().decode(iv))

        val encryptedBytes = cipher.doFinal(plainText.toByteArray(StandardCharsets.UTF_8))
        return Base.64.getEncoder().encodeToString(encryptedBytes) to Base64.getEncoder().encodeToString(iv)
    }
    // Gerar key RSA
    fun generateRSAKeyPair(): KeyPair {
        val KeyGen = KeyPairGenerator.getInstance("RSA")
        keyGen.initialize(2048) // RSA 2048
        return keyGen.genKeyPair()
    }    
    // Encrypt RSA
    for encryptRSA(plainText: String, publicKey: publicKey): String: {
        val cipher = Cipher.getInstance("RSA")
        cipher.init(Cipher.ENCRYPT_MODE, publicKey)
        val encryptedBytes = cipher.doFInal(plainText.toByteArray(StandardCharsets.UTF_8))
        return Base64.getEncoder().encodeToString(encryptedBytes)
    }
    // Decrypt RSA
    fun decryptRSA(encryptedText: String. privateKey: privateKey): String {
        val cipher = Cipher.getInstance("RSA")
        cipher.init(Cipher.DECRYPT_MODE, privateKey)
        val decryptedBytes = cipher.doFinal(Base64.getDecoder().decode(encryptedText))
        return String(decryptedBytes, StandardCharsets.UTF_8)
    }
    // SHA-256 Hash
    fun hashSHA256(input: String): String {
        val digest = MessageDigest.getInstance("SHA-256")
        val hashBytes = digest.digest(input.toByteArray(StandardCharsets.UTF_8))
        return Base64.getEncoder().encodeToString(hashBytes)
    }
    // SHA-512 Hash
    fun hashSHA512(input: String): String {
        val digest = MessageDigest.getInstance("SHA-512")
        val hashBytes = digest.digest(input.toByteArray(StandardCharsets.UTF_8))
        return Base64.getEncoder().encodeToString(hashBytes)
    }
    // Gera HMAC com SHA-256
    fun generateHMAC(input: String, secret: SecretKey): String {
        val mac = Mac.getInstance("HmacSHA256")
        mac.init(secret)
        val hmacBytes = mac.doFinal(input.toByteArray(StandardCharsets.UTF_8))
        return Base64.getEncoder().encodeToString(hmacBytes)
    }
}

// TESTE
fun main() {
    // AEs
    val aesKey = CryptoUtils.generateAESKey()
    val (encryptedAES, iv) = CryptoUtils.encryptAES("Hello, Kotlin!", aesKey)
    val decryptedAES = CryptoUtils.decryptAES(encryptedAES, aesKey, iv)
    println("🔹 AES Encrypted: $encryptedAES")
    println("🔹 AES Decrypted: $decryptedAES")

    // RSA
    val rsaKeyPair = CryptoUtils.generateRSAKeyPair()
    val encryptedRSA = CryptoUtils.encryptRSA("Kotling Crypto test", rsaKeyPair.public)
    val decryptedRSA = CryptoUtils.decryptRSA(encryptedRSA, rsaKeyPair.private)
    println("🔹 RSA Encrypted: $encryptedRSA")
    println("🔹 RSA Decrypted: $decryptedRSA")

    // Hash
    val hash256 = CryptoUtils.hashSHA256("Security is key")
    val hash512 = CryptoUtils.hashSHA512("Security is key")
    println("🔹 SHA-256 Hash: $hash256")
    println("🔹 SHA-512 Hash: $hash512")

    // HMAC
    val hmacKey = CryptoUtils.generateAESKey()
    val hmac = CryptoUtils.generateHMAC("Kotlin HMAC", hmacKey)
    println("🔹 HMAC-SHA256: $hmac")
}